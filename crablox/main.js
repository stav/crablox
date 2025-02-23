// import htmx from 'htmx.org';

function crbOpenBlock (openButton) {
  const item = openButton.closest('.item')
  // Reveal data block
  const data = item.querySelector(`.wlv-data`)
  data.style.display = 'inline-block'
  // Reveal clear button
  const clearButton = item.querySelector('.wlv-clear')
  clearButton.style.display = 'inline-block'
}
function crbClearBlock (clearButton) {
  // Hide clear button
  clearButton.style.display = 'none'
  // Hide data block
  const item = clearButton.closest('.item')
  const data = item.querySelector(`.wlv-data`)
  data.style.display = 'none'
}
function crbCloseBlock (closeButton) {
  const slot = closeButton.closest('.slot')
  slot.outerHTML = ''
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
