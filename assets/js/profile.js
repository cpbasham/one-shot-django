$("a.delete").on("click", function(e) {
  var target = $(e.target);
  var id = target.parents("tr").find("td:first-child").html();
  $.ajax({
    url: "/item_sets/" + id,
    method: "DELETE"
  }).done(function(data) {
    target.closest("tr").remove();
  });
});