inputImage = document.getElementById("input-image")
imageContainer = document.getElementById("image-container");
drawingCanvas = document.getElementById("drawing-canvas");
imageDisplayBox = document.getElementById("image-display-box")
const paletteContainer = document.getElementById("palette-container")
const colorSwatchesGrid = document.querySelector(".color-swatches-grid");
const context = drawingCanvas.getContext('2d')

// to reset the name of the file in the image input field
inputImage.value = "";
imageDisplayBox.filled = false;


const MAX_CANVAS_SIZE = 200;
const QUANTIZATION_FACTOR = 15;
const NUM_COLORS_IN_PALETTE = 8;

function rgbToHex(r, g, b) {
    const toHex = (c) => c.toString(16).padStart(2, '0');
    return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

function getLuminance(r, g, b) {
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255;
}


function drawImageInCanvas() {
    imageDisplayBox.filled = true;
    const originalWidth = imageContainer.naturalWidth;
    const originalHeight = imageContainer.naturalHeight;
    let targetWidth;
    let targetHeight;

    if (originalWidth > originalHeight) {
        targetWidth = MAX_CANVAS_SIZE;
        targetHeight = (MAX_CANVAS_SIZE * originalHeight) / originalWidth;
    } else {
        targetHeight = MAX_CANVAS_SIZE;
        targetWidth = (MAX_CANVAS_SIZE * originalWidth) / originalHeight;
    }
    
    drawingCanvas.width = targetWidth;
    drawingCanvas.height = targetHeight;

    context.drawImage(imageContainer, 0, 0, targetWidth, targetHeight);
}

function extractPaletteColors() {
    const imageData = context.getImageData(0, 0, drawingCanvas.width, drawingCanvas.height);
    const pixels = imageData.data;

    const colorMap = new Map();
    const sampleRate = 5;

    for (let i = 0; i < pixels.length; i += 4 * sampleRate) {
        const r = pixels[i];
        const g = pixels[i + 1];
        const b = pixels[i + 2];
        // const alpha = pixels[i + 3];

        const quantizedR = Math.floor(r / QUANTIZATION_FACTOR) * QUANTIZATION_FACTOR;
        const quantizedG = Math.floor(g / QUANTIZATION_FACTOR) * QUANTIZATION_FACTOR;
        const quantizedB = Math.floor(b / QUANTIZATION_FACTOR) * QUANTIZATION_FACTOR;
        const colorKey = `${quantizedR},${quantizedG},${quantizedB}`;
        colorMap.set(colorKey, (colorMap.get(colorKey) || 0) + 1);
    }

    const sortedColors = Array.from(colorMap.entries()).map(
        ([colorKey, count]) => {
            const [r, g, b] = colorKey.split(',').map(Number);
            return { r, g, b, count };
        }
    ).sort((a, b) => b.count - a.count).slice(0, NUM_COLORS_IN_PALETTE);
    
    return sortedColors;
}

function displayPalette(hexColors) {
    colorSwatchesGrid.innerHTML = '';
    hexColors.forEach(hexColor => {
        const swatch = document.createElement('div');
        swatch.classList.add('color-swatch');
        swatch.style.backgroundColor = hexColor;

        const hexSpan = document.createElement('span');
        hexSpan.textContent = hexColor.toUpperCase();
        const r = parseInt(hexColor.substring(1, 3), 16);
        const g = parseInt(hexColor.substring(3, 5), 16);
        const b = parseInt(hexColor.substring(5, 7), 16);
        hexSpan.style.color = getLuminance(r, g, b) > 0.5 ? '#333' : '#eee';
        swatch.appendChild(hexSpan);

        swatch.addEventListener('click', () => {
            navigator.clipboard.writeText(hexColor.toUpperCase()).then(
                () => {
                    const originalText = hexSpan.textContent;
                    hexSpan.textContent = "Copied To Clipboard";
                    setTimeout(() => {
                        hexSpan.textContent = originalText;
                    }, 1000);
                }
            ).catch(err => {
                console.log(`could not copy text. error: ${err}`);
            })
        })

        colorSwatchesGrid.appendChild(swatch);
    });

    paletteContainer.style.display = 'block';
}

inputImage.addEventListener('change', function (event) {
    tempImage = event.target.files[0];
    
    if (tempImage) {
        const reader = new FileReader();

        reader.addEventListener('load', function () {
            // this function runs after the file is fully loaded by the reader
            imageContainer.src = reader.result;

            imageContainer.onload = function () {
                drawImageInCanvas();
                const sortedRgbColors = extractPaletteColors();
                const hexPalette = sortedRgbColors.map(color => rgbToHex(color.r, color.g, color.b));
                console.log("Hex Palette: " + hexPalette);

                displayPalette(hexPalette);
            }
        });

        reader.readAsDataURL(tempImage);
    }

})
