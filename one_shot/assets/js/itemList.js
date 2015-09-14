var itemDiv = $("div.items");
var itemSearch = itemDiv.find("#item-search");
var images = itemDiv.find("ul.images li span");

function searchForItem(str) {
  images = itemDiv.find("ul.images li span");
  var pattern = new RegExp(escapeRegExp(str.toLowerCase()));
  images.each(function(i) {
    var image = $(images[i]);
    if (nameMatch(pattern, image) || image.data("purchasable") === "false") {
      image.parent().hide();
    } else {
      image.parent().show();
    }
  });
}

itemSearch.on("input", function(e) {
  searchForItem(e.target.value);
});

images.draggable({helper: 'clone'});


function nameMatch(pattern, image) {
  return !pattern.test(normalize(image.attr("title")))
}

function escapeRegExp(str) {
  return str.replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
}

function normalize(str) {
  return str.replace(/\W|\d/gi, "").toLowerCase();
}
