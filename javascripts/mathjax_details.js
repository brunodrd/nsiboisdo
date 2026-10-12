// Composer les formules d'un bloc dépliable (??? / <details>) au moment où on l'ouvre.
// L'événement « toggle » ne remonte pas dans le document : on l'écoute en phase de capture (true).
document.addEventListener("toggle", function (event) {
  const bloc = event.target;
  if (bloc.tagName === "DETAILS" && bloc.open && window.MathJax && MathJax.typesetPromise) {
    MathJax.typesetPromise([bloc]);
  }
}, true);
