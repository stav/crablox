/**
 * @module main
 * @description UI interactions and setup.
 *
 * Opening and closing blocks, managing a lightbox, and initializing the Swapy library.
 */

// BLOCKS

/**
 * Opens a data block and reveals the clear button within a specified item.
 *
 * @param {HTMLElement} openButton - The button element that triggers the opening of the data block.
 */
function crbOpenBlock (openButton) {
  const item = openButton.closest('.item')
  // Reveal data block
  const data = item.querySelector(`.wlv-data`)
  data.style.display = 'inline-block'
  data.scrollTop = 0
  // Reveal lightbox button
  if (item.querySelector('.cbx_image')) {
    const lightboxButton = item.querySelector('.wlv-lightbox')
    lightboxButton.style.display = 'inline-block'
  }
  // Reveal clear button
  const clearButton = item.querySelector('.wlv-clear')
  clearButton.style.display = 'inline-block'
  // Reveal history button
  const historyButton = item.querySelector('.wlv-history')
  if ('history' in historyButton.dataset) {
    historyButton.style.display = 'inline-block'
  }
}

/**
 * Clears and hides a data block and its associated clear button.
 *
 * @param {HTMLElement} clearButton - The clear button element that triggers the clear action.
 */
function crbClearBlock (clearButton) {
  // Hide clear button
  clearButton.style.display = 'none'
  // Hide data block
  const item = clearButton.closest('.item')
  const data = item.querySelector(`.wlv-data`)
  data.innerHTML = ''
  // Hide lightbox button
  const lightboxButton = item.querySelector('.wlv-lightbox')
  lightboxButton.style.display = 'none'
}

function doLightbox (lightboxButton) {
  // Open lightbox
  const item = lightboxButton.closest('.item')
  const image = item.querySelector('.cbx_image')
  openLightbox(image.parentElement)
}

function crbOpenHistory (historyButton) {
  // Hide lightbox button
  const item = historyButton.closest('.item')
  const lightboxButton = item.querySelector('.wlv-lightbox')
  lightboxButton.style.display = 'none'
}

/**
 * Closes and removes the closest parent element with the class 'slot' of the given close button.
 *
 * @param {HTMLElement} closeButton - The button element that triggers the close action.
 */
function crbCloseBlock (closeButton) {
  const slot = closeButton.closest('.slot')
  slot.outerHTML = ''
}

/**
 * Updates the first button with the value of the ticker input.
 *
 * @param {HTMLElement} form - The form element.
 * @param {string} ticker - The ticker value.
 */
function crbUpdateTicker (form, ticker) {
  const blockItem = form.closest('.item')
  const tickerButton = blockItem.querySelector('.crb-buttons button')
  tickerButton.innerHTML = ticker.toUpperCase()
}

// LIGHTBOX

/**
 * Opens a lightbox with the image, caption, and details from the provided wrapper element.
 *
 * https://www.bualabs.com/archives/5073/displaying-cloudinary-images-in-fasthtml-ep-3/
 *
 * @param {HTMLElement} wrapper - The wrapper element containing the image and details to display in the lightbox.
 */
function openLightbox (wrapper) {
  // Image
  const image = wrapper.querySelector('img')
  const imageUrl = image.getAttribute('src')
  const caption = image.getAttribute('alt')
  document.getElementById('lightbox-img').src = imageUrl
  document.getElementById('lightbox-cap').innerHTML = caption
  // Details
  const item = wrapper.closest('.item')
  const details = item.querySelector('.wlv-details')
  document.getElementById('lightbox-det').innerHTML = details.innerHTML
  document.getElementById('lightbox').style.display = 'flex'
}

/**
 * Shows the lightbox for time series data by hiding the image and caption elements.
 */
function showTimeSeriesLightbox() {
  document.getElementById('lightbox-img').style.display = 'none'
  document.getElementById('lightbox-cap').style.display = 'none'
  document.getElementById('lightbox-det').innerHTML = '<h1 style="display: flex; align-items: center; height: 100dvh">Loading...</h1>'
  document.getElementById('lightbox').style.display = 'flex'
}

/**
 * Hides the lightbox element by setting its display style to 'none'.
 */
function closeLightbox () {
  document.getElementById('lightbox-img').style.display = ''
  document.getElementById('lightbox-cap').style.display = ''
  document.getElementById('lightbox').style.display = 'none'
}

/**
 * Listen for keyboard events: escape closes lightbox
 */
document.addEventListener('keydown', function (event) {
  console.log(event.key)
  if (event.key === 'Escape') {
    closeLightbox()
  }
})

// SWAPY

/**
 * The container to hold the #block-grid and all subsequent Swapy slots.
 */
const container = document.querySelector('.swapy-container')

/**
 * @type {import("../vendor/swapy/swapy").Config}
 */
const options = {
  animation: 'dynamic',
  enabled: true
}

/**
 * The global Swapy object is created by swapy.min.js via swapy.js.
 *
 * @typedef {Object} Swapy
 * @property {function} createSwapy
 * @property {function} getClosestScrollableContainer
 * @property {Object} utils
 *
 * @global Swapy
 * @type {Swapy}
 */
var Swapy

/**
 * The `createSwapy` function returns an object with a `Swapy` interface.
 * This `Swapy` interface is different than the global `Swapy` object.
 *
 * @type {import("../vendor/swapy/swapy").Swapy}
 */
const swapy = Swapy.createSwapy(container, options)
