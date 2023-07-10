setTimeout(() => {
    document.querySelector('#alerta').style.display = 'none'
}, 5000)

const inputFile = document.querySelector(".fileContainer");
const pictureImage = document.querySelector(".img-fluid");
const pictureImageTxt = "";


inputFile.addEventListener("change", function (e) {
  const inputTarget = e.target;
  console.log(inputTarget)
  const file = inputTarget.files[0];

  if (file) {
    const reader = new FileReader();

    reader.addEventListener("load", function (e) {
      const readerTarget = e.target;
      const img = document.createElement("img");
      img.style.width = "100px";
      img.src = readerTarget.result;
      img.classList.add("img-fluid");

      pictureImage.innerHTML = "";
      pictureImage.appendChild(img);
    });

    reader.readAsDataURL(file);
  } else {
    pictureImage.innerHTML = pictureImageTxt;
  }
});
