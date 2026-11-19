// When the URL #fragment targets an element inside collapsed <details>,
// expand all enclosing <details> (and the target's own first <details>,
// if any) so the target is visible, then scroll to it.
(function () {
  function openTargetDetails() {
    if (!location.hash) return;
    var target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!target) return;
    for (var el = target; el; el = el.parentElement) {
      if (el.tagName === "DETAILS") el.open = true;
    }
    var inner = target.querySelector("details");
    if (inner) inner.open = true;
    target.scrollIntoView();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", openTargetDetails);
  } else {
    openTargetDetails();
  }
  window.addEventListener("hashchange", openTargetDetails);
})();
