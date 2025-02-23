// import htmx from 'htmx.org';

function crbCloseBlock (closeButton) {
  // Hide close button
  closeButton.style.display = 'none'
  // Hide data block
  const item = closeButton.parentElement.parentElement
  const data = item.querySelector(`.wlv-data`)
  data.style.display = 'none'
}
function crbOpenBlock (openButton) {
  // Reveal data block
  const item = openButton.parentElement.parentElement
  const data = item.querySelector(`.wlv-data`)
  data.style.display = 'inline-block'
  // Reveal close button
  const closeButton = openButton.parentElement.querySelector('.wlv-close')
  closeButton.style.display = 'inline-block'
}

// https://www.bualabs.com/archives/5073/displaying-cloudinary-images-in-fasthtml-ep-3/
function openLightbox (wrapper) {
  // Image
  const image = wrapper.querySelector('img')
  const imageUrl = image.getAttribute('src')
  const caption = image.getAttribute('alt')
  document.getElementById('lightbox-img').src = imageUrl
  document.getElementById('lightbox-cap').innerHTML = caption
  // Article
  const item = wrapper.closest('.item')
  const details = item.querySelector(`.wlv-data`)
  const article = details.querySelector('article')
  document.getElementById('lightbox-det').innerHTML = article.innerHTML
  document.getElementById('lightbox').style.display = 'flex'
}
function closeLightbox () {
  document.getElementById('lightbox').style.display = 'none'
}
document.addEventListener('keydown', function (event) {
  console.log(event.key)
  if (event.key === 'Escape') {
    closeLightbox()
  }
})

// Swapy
const container = document.querySelector('.swapy-container')
const swapy = Swapy.createSwapy(container, {
  animation: 'dynamic'
  // swapMode: 'drop',
  // autoScrollOnDrag: true,
  // enabled: true,
  // dragAxis: 'x',
  // dragOnHold: true
})
swapy.enable(true)
