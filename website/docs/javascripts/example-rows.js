// Make each row of an example table open that example's website.
// Applies to tables with an "Explore" column; clicks on the row's own links still work normally.
function linkExampleRows() {
  document.querySelectorAll("article table").forEach((table) => {
    const headers = [...table.querySelectorAll("thead th")].map((th) => th.textContent.trim());
    const col = headers.indexOf("Explore");
    if (col === -1) return;
    table.querySelectorAll("tbody tr").forEach((row) => {
      const link = row.children[col]?.querySelector("a");
      if (!link) return;
      row.classList.add("example-row");
      row.addEventListener("click", (event) => {
        if (event.target.closest("a")) return;
        window.location.href = link.href;
      });
    });
  });
}

if (typeof document$ !== "undefined") {
  document$.subscribe(linkExampleRows);
} else {
  document.addEventListener("DOMContentLoaded", linkExampleRows);
}
