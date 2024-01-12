import { getData } from "./data.js";
import { load } from "./load.js";
import { dom, inp } from "./dom.js";
import { sortCards } from "./sort.js";

const data = getData();
const selectors = dom();
console.log(data);
console.log(selectors);
load(data, selectors);

selectors.toggle.value = 'notGold'

selectors.form.addEventListener("submit", (e) => {
  e.preventDefault();
  let inputs = inp(selectors);
  sortCards(inputs, selectors, data);
});

selectors.toggle.addEventListener("click", () => {
  let inputs = inp(selectors);
  const btn = selectors.toggle;
  if (btn.value === "notGold") {
    let d = getData()
    let cost = getData().map((obj) => obj.cost * 2);
    btn.value = "Gold";
    console.log("toggling to gold");
    d.forEach((card, i) => {
      card.cost = cost[i];
    });
    console.log(d, data)
    sortCards(inputs,selectors,d)
    document.body.classList.remove('dark')
    document.body.classList.add('gold')

  } else {
    btn.value = "notGold";
    console.log("toggling off gold");
    sortCards(inputs,selectors, getData())
    document.body.classList.remove('gold')
    document.body.classList.add('dark')
  }
});
