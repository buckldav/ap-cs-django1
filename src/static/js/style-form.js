// Style the comment form
$(`[for="id_comment"],#id_comment`).wrapAll(`<div class="form-group"></div>`)
$(`[for="id_name"],#id_name,button[type="submit"]`).wrapAll(`<div class="form-group row mx-0"></div>`)
$(`[for="id_name"]`).addClass("py-2 pr-2")
$(`#id_name`).addClass("form-control col-sm-4")
$(`#id_comment`).addClass("form-control").removeAttr("cols").attr("rows", 3)
$(`button[type=submit]`).addClass("mt-3 mx-sm-2 mt-sm-0").css("height", "38px")