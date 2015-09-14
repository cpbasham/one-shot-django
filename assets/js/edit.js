var lis = $("li[data-top='true']");
// console.log(lis);

// console.log(e);
bringToTop($(lis[0]));
$(lis[0]).data("top", "");
bringToTop($(lis[1]));
$(lis[1]).data("top", "");

specifyItemsByMap($(lis[0]).data("map"), "");


var newRow = $("div.row-items");
newRow.find("ul").droppable({drop: itemSetReceiver});