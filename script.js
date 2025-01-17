function addEntryField(groupClass, fieldName, placeholderText) {
    const group = document.querySelector(groupClass);
    const entry = document.createElement('div');
    entry.classList.add('entry');

    const newInput = document.createElement('input');
    newInput.setAttribute('type', 'text');
    newInput.setAttribute('name', `${fieldName}[]`);
    newInput.setAttribute('placeholder', placeholderText);
    newInput.setAttribute('required', true);

    const removeButton = document.createElement('button');
    removeButton.setAttribute('type', 'button');
    removeButton.classList.add('remove-entry');
    removeButton.textContent = 'Remove';
    removeButton.onclick = function() {
        group.removeChild(entry);
    };

    entry.appendChild(newInput);
    entry.appendChild(removeButton);
    group.appendChild(entry);
}

function addTextareaField(groupClass, fieldName, placeholderText) {
    const group = document.querySelector(groupClass);
    const entry = document.createElement('div');
    entry.classList.add('entry');

    const newTextarea = document.createElement('textarea');
    newTextarea.setAttribute('name', `${fieldName}[]`);
    newTextarea.setAttribute('rows', '3');
    newTextarea.setAttribute('placeholder', placeholderText);
    newTextarea.setAttribute('required', true);

    const removeButton = document.createElement('button');
    removeButton.setAttribute('type', 'button');
    removeButton.classList.add('remove-entry');
    removeButton.textContent = 'Remove';
    removeButton.onclick = function() {
        group.removeChild(entry);
    };

    entry.appendChild(newTextarea);
    entry.appendChild(removeButton);
    group.appendChild(entry);
}