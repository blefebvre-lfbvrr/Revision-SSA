// Révision SSA hors ligne : réseau d'abord (toujours la dernière version des questions),
// cache en secours. Les polices Google, qui ne changent pas, sont servies depuis le cache.
var CACHE = "revision-ssa-v1";
var CORE = ["./", "index.html", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png", "icons/apple-touch-icon.png"];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function put(req, res) {
  if (res && (res.ok || res.type === "opaque")) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
  return res;
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);
  if (url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com") {
    e.respondWith(caches.match(req).then(function (hit) { return hit || fetch(req).then(function (res) { return put(req, res); }); }));
    return;
  }
  if (url.origin !== self.location.origin) return;
  e.respondWith(fetch(req).then(function (res) { return put(req, res); }).catch(function () {
    return caches.match(req, { ignoreSearch: true }).then(function (hit) {
      return hit || (req.mode === "navigate" ? caches.match("./") : Response.error());
    });
  }));
});
