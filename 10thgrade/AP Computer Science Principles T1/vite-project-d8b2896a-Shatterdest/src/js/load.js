export function load(data, s) {
  for (let i = 0; i < data.length; i++) {
    const cardLayout = `<div class="card">
        <h3 class="display-name">${data[i].displayName}</h3>
        <img src="${data[i].displayIconSmall}" class='img' alt='This card is about: ${data[i].displayName}'>
        <img src="${data[i].role.displayIcon}" class='class-img' alt='Agent Class is: ${data[i].role.displayName}'><h3 class="agent-type">${data[i].role.displayName}</h3>
        <p class="cost">${data[i].cost} Credits</p>
        <p class="description">${data[i].description}</p>
        </div>`;
    console.log(`Loading ${data[i].displayName}`);
    s.container.insertAdjacentHTML("beforeend", cardLayout);
  }
}
