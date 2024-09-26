//скрипт для увеличения фотографии при нажатии https://ru.stackoverflow.com/questions/1213353/%D0%9A%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D1%83%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BF%D1%80%D0%B8-%D0%BD%D0%B0%D0%B6%D0%B0%D1%82%D0%B8%D0%B8-%D1%81-%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%B1%D0%B5%D0%BB%D0%BE%D0%B9-%D1%80%D0%B0%D0%BC%D0%BA%D0%B8-%D0%B2%D0%BE%D0%BA%D1%80%D1%83%D0%B3-%D0%BA%D0%B0%D1%80%D1%82
function open_photo(photo) {
  document.getElementById("big-photo").innerHTML =
    ("<img onclick='close_photo()' src='" + photo + "'>")
}

function close_photo() {
  document.getElementById("big-photo").innerHTML = ""
}
//style='position: absolute;