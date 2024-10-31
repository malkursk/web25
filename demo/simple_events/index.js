const minus = document.getElementById("minus")
const plus = document.getElementById("plus")

const box = document.getElementById("box")
const field = document.getElementById("field")
const info = document.getElementById("info")

const logBtn = document.getElementById("logBtn")
field.value = 500

const getCounter = (initValue) => {
    let value = initValue

    const plus = () => {
        value++
        console.log(value);
    }

    const minus = () => {
        value--
        console.log(value);
    }

    const getValue = () => value

    const updateValue = (newValue) => {
        value = newValue
    }

    return {
        updateValue,
        getValue,
        plus,
        minus
    }
}

const counter = getCounter(field.value)

const updateFieldValue = () => {
    field.value = counter.getValue()
}

minus.addEventListener("click", () => {
    counter.minus()
    field.value = counter.getValue()
})

plus.addEventListener("click", () => {
    counter.plus()
    field.value = counter.getValue()
})

field.onchange = (event) =>{
    counter.updateValue(event.target.value)
}

logBtn.addEventListener("click", () => {
    info.textContent = `counter: ${counter.getValue()}, agree: ${box.checked}`
})