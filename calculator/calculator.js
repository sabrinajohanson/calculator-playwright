let current = '0'
let previous = null
let op = null

function render() {
    document.querySelector('[data-testid="result"]').textContent = current
}

function digit(value) {
    if (current === '0') {
        current = value    
    } else {
        current = current + value
    }
    render() 
}

function operator(value) {
    previous = current
    current = '0'
    op = value
}

function equals() {
    const a = parseFloat(previous)
    const b = parseFloat(current)

    if (op === '+') current = String(a + b)
    if (op === '-') current = String(a - b)
    if (op === '*') current = String(a * b)
    if (op === '/') current = String(a / b)

    previous = null
    op = null
    render()
}

function clearALL() {
    current = '0'
    previous = null
    op = null
    render()
}

function sign() {
  current = String(parseFloat(current) * -1)
  render()
}

function percent() {
  current = String(parseFloat(current) / 100)
  render()
}

function dot() {
  if (!current.includes('.')) {
    current = current + '.'
  }
  render()
}