// import htmx from 'htmx.org';

function crbCloseBlock (id) {
  document.getElementById(`wlv-${id}-data`).innerHTML = ''
  document.getElementById(`wlv-${id}-close-button`).style.display = 'none'
  document.getElementById(`wlv-${id}-toggle-button`).style.display = 'none'
}
function crbToggleDetails (id) {
  const el = document.querySelector(`#${id} article`)
  const display = el.style.display
  el.style.display =
    display === 'none' || display === '' ? 'inline-block' : 'none'
}
function crbOpenBlock (id, path) {
  console.log('OPEN - crbOpenBlock()', id, path)

  // Reveal close button
  const cb = document.getElementById(`wlv-${id}-close-button`)
  console.log('>a', id, cb.style.display, cb)
  cb.style.display = 'inline-block'
  console.log('>b', id, cb.style.display, cb)

  const target = `#wlv-${id}-data`
  const data = document.querySelector(target)
  console.log('>c', target, data)

  // Ajax request:
  //  1. Do an API GET for the given path,
  //  2. Target the id's data element,
  //  3. Wait for the callback to reveal the toggle button
  htmx.ajax('GET', path, { target }).then(e => {
    const el = document.querySelector(`#${id} article`)
    console.log('CALLback', id, el)
    if (el) {
      document.getElementById(`wlv-${id}-toggle-button`).style.display =
        'inline-block'
    }
  })
}

// https://www.bualabs.com/archives/5073/displaying-cloudinary-images-in-fasthtml-ep-3/
function openLightbox (imageUrl) {
  document.getElementById('lightbox-img').src = imageUrl
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
