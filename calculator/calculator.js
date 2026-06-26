let history = ''
let currentNumber = ''
let pendingOp = null
let pendingValue = null
let justCalculated = false

function render() {
  const display = currentNumber === '' ? 
    (pendingValue !== null ? String(pendingValue) : '0') 
    : currentNumber
  document.querySelector('[data-testid="result"]').textContent = display
  document.querySelector('[data-testid="expression"]').textContent = history
}

function digit(value) {
  // Limit input to 15 digits (excluding dot and negative sign)
  const digits = currentNumber.replace('.', '').replace('-', '')
  if (digits.length >= 15) return

  if (justCalculated) {
    history = ''
    currentNumber = value
    justCalculated = false
  } else {
    currentNumber = currentNumber === '' ? value : currentNumber + value
  }
  render()
}

function dot() {
  if (justCalculated) {
    history = ''
    currentNumber = '0.'
    justCalculated = false
    render()
    return
  }
  if (!currentNumber.includes('.')) {
    currentNumber = (currentNumber === '' ? '0' : currentNumber) + '.'
  }
  render()
}

function operator(op) {
  justCalculated = false

  if (currentNumber !== '') {
    if (pendingOp !== null) {
    // Calculate the accumulated result
      const result = calculate(pendingValue, pendingOp, parseFloat(currentNumber))
      pendingValue = result
      history = history + currentNumber + ' ' + op + ' '
    } else {
      pendingValue = parseFloat(currentNumber)
      history = currentNumber + ' ' + op + ' '
    }
    currentNumber = ''
    pendingOp = op
  } else {
    // Operator changed before typing a new number
    history = history.trimEnd().slice(0, -1) + op + ' '
    pendingOp = op
  }

  render()
}

function equals() {
  if (pendingOp === null || currentNumber === '') return

  const result = calculate(pendingValue, pendingOp, parseFloat(currentNumber))

  // History shows the full expression
  history = history + currentNumber + ' ='

  // Result appears below
  currentNumber = String(result)
  pendingOp = null
  pendingValue = null
  justCalculated = true

  render()
}

function calculate(a, op, b) {
  if (op === '+') return a + b
  if (op === '-') return a - b
  if (op === '*') return a * b
  if (op === '/') {
    if (b === 0) return 'Erro'
    return a / b
  }
}

function clearALL() {
  history = ''
  currentNumber = ''
  pendingOp = null
  pendingValue = null
  justCalculated = false
  render()
}

function backspace() {
  // Allow backspace on result, but clear history and disable justCalculated flag
  if (justCalculated) {
    history = ''
    justCalculated = false
  }
  currentNumber = currentNumber.slice(0, -1)
  render()
}

function sign() {
  if (currentNumber === '' || currentNumber === '0') return
  if (currentNumber.startsWith('-')) {
    currentNumber = currentNumber.slice(1)
  } else {
    currentNumber = '-' + currentNumber
  }
  render()
}

function percent() {
  if (currentNumber === '') return

  if (pendingValue !== null) {
    // Calculate % relative to the previous number
    currentNumber = String(pendingValue * parseFloat(currentNumber) / 100)
  } else {
    // No pending operation, just divide by 100
    currentNumber = String(parseFloat(currentNumber) / 100)
  }
  render()
}
