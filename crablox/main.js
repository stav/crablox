// import htmx from 'htmx.org';

function crbCloseBlock (id) {
  document.getElementById(`wlv-${id}-data`).innerHTML = ''
  document.getElementById(`wlv-${id}-close-button`).style.display = 'none'
  document.getElementById(`wlv-${id}-toggle-button`).style.display = 'none'
}
function crbOpenBlock (id, path) {
  // Reveal close button
  const cb = document.getElementById(`wlv-${id}-close-button`)
  cb.style.display = 'inline-block'
}

// https://www.bualabs.com/archives/5073/displaying-cloudinary-images-in-fasthtml-ep-3/
function openLightbox (wrapper) {
  const image = wrapper.querySelector('img')
  const imageUrl = image.getAttribute('src')
  const caption = image.getAttribute('alt')
  const id = wrapper.getAttribute('data-id')
  const details = document.getElementById(id)
  const article = details.querySelector('article')
  document.getElementById('lightbox-img').src = imageUrl
  document.getElementById('lightbox-cap').innerHTML = caption
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
