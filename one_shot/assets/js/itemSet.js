// DON'T ALLOW SELECTION OF +
$("div.item-set-container").on("selectstart dragstart", "div.new-row, div.row-items, div.item-set-row-delete", function(evt) {
  evt.preventDefault();
  return false;
});

$("div.item-set-container").on("click", "div.new-row", function(evt) {
  evt.preventDefault();
  var target = $(evt.target).prev();
  $.ajax({
    url: "/item_sets/" + currentSetId() + "/item_categories/new",
    method: "GET",
    dataType: "html"
  }).done(function(data) {
    var newRow = $(data).appendTo(target);
    newRow.find("ul").droppable({drop: itemSetReceiver});
  });
});

function itemSetReceiver( e, ui ) {
  e.preventDefault();
  e.stopPropagation();
  var li = $('<li><span data-type="item" data-api-id="' + ui.draggable.data("id") + '" title="' + ui.draggable.attr("title") + '" style="' + ui.draggable.attr("style") + '" class="sprite"></span></li>');
  li.appendTo(e.target);
  var categoryId = li.parents("div.item-set-row-container").data("rowId");
  $.ajax({
    url: "/item_categories/" + categoryId + "/items",
    method: "POST",
    data: "item_id=" + ui.draggable.data("id"),
    dataType: "json"
  }).done(function(data) {
    li.find("span").data("id", data["id"]);
  });
  // console.log(li.parents("div.item-set-row-container"));
  // console.log(ui.helper);
}

$("div.item-set-container").on("dblclick", "span.sprite", function(e) {
  var target = $(e.target);
  var id = target.data("id");
  $.ajax({
    url: "/items/" + id,
    method: "DELETE"
  }).done(function() {
    target.parent().remove();
  });
});

$("div.item-set-container").on("click", "div.item-set-row-container div.row-items", function(e) {
  var container = $(e.target).closest("div.item-set-row-container");
  container.find("div.item-set-row-delete").toggle();
  container.siblings().find("div.item-set-row-delete").hide();
});

$("div.item-set-container").on("dblclick", "div.item-set-row-delete", function(e) {
  var row = $(e.target).parent();
  $.ajax({
    url: "/item_categories/" + row.data("rowId"),
    method: "DELETE"
  }).done(function() {
    row.remove();
  });
});


window.onbeforeunload = function() {
  updateSetName;
  $(".item-set-row-container").each(function() {
    updateCategoryName($(this));
  });
}

$("input.item-set-name").on("blur", function(e) {
  updateSetName();
});
function updateSetName() {
  $.ajax({
    url: "/item_sets/" + currentSetId(),
    method: "POST",
    data: "name=" + $("input.item-set-name").val()
  });
  return null;
}
$("div.item-set-container").on("blur", ".item-set-row-container input", function(e) {
  updateCategoryName($(e.target).parent());
});
function updateCategoryName(category) {
  var rowId = category.data("rowId");
  $.ajax({
    url: "/item_categories/" + rowId,
    method: "POST",
    data: "name=" + category.find("input").val()
  });
  return null;
}


// function showText(text) {
//   $("body").empty().html(text);
// }

// $.ajax({
//   url: "items/",
//   method: "GET",
//   dataType: "json"
// }).done(function(data) {
//   // showText(JSON.stringify(data));
//   // showText(data.TT);
//   console.log(data.SR);
// })
