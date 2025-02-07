from fasthtml.common import Style


styles = Style(
    """
    .container {
        max-width: 95%;
    }
    .wlv-block {
        display: inline-block;
        border: 1px solid #ccc;
        padding: 1em;
        margin: 0.5em;
        max-width: 100%;
    }
    .wlv-data {
        max-width: 400px;
    }
    .wlv-data .cbx_image {
        max-width: 100%;
        cursor: pointer;
    }
    .wlv-details {
        display: none;
        max-width: 400px;
    }
    .wlv-toggle {
        display: none;
        background-color: #43c436;
    }
    .wlv-close {
        display: none;
        margin-left: 1em;
        background-color: #c44336;
    }

    /* (Lightbox) */
    .lightbox {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.8);
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }
    .lightbox-image {
        max-width: 90%;
        max-height: 80%;
    }
    .lightbox-close {
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 2rem;
        color: #fff;
        cursor: pointer;
    }
"""
)
