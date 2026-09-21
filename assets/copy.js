/* The copy button on a prompt block.

   ONE JOB AND NO DEPENDENCIES. Every prompt on this site is written to be pasted into
   somebody else's session, so the page offers to put it on the clipboard. The text is
   already visible and selectable above the button: this saves a drag, it is not the only
   way to get the prompt, and the page works with this file blocked.

   The clipboard API needs a secure context and a user gesture. Both hold here, and the
   fallback path covers the browser that refuses anyway. */
document.addEventListener('click', function (e) {
  var btn = e.target.closest('[data-copy]');
  if (!btn) return;
  var fig = btn.closest('figure');
  var pre = fig && fig.querySelector('pre');
  if (!pre) return;
  var text = pre.textContent;
  var done = function (ok) {
    var was = btn.textContent;
    btn.textContent = ok ? 'Copied' : 'Press Ctrl C to copy';
    btn.classList.add('ok');
    setTimeout(function () { btn.textContent = was; btn.classList.remove('ok'); }, 2200);
  };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(function () { done(true); },
                                             function () { select(pre); done(false); });
  } else {
    select(pre);
    done(false);
  }
  function select(el) {
    var r = document.createRange();
    r.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(r);
  }
});
