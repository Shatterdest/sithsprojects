export function dom() {
  const selectors = {
    form: document.getElementById("form"),
    submit: document.getElementById("submit"),
    container: document.getElementById("container"),
    duelist: document.getElementById('duelist'),
    initiator: document.getElementById('initiator'),
    controller: document.getElementById('controller'),
    sentinel: document.getElementById('sentinel'),
    toggle: document.getElementById('cb3-8')
  };
  return selectors;
}

export function inp(selectors){
  const inp = {
    duelist: selectors.duelist.checked,
    initiator: selectors.initiator.checked,
    controller: selectors.controller.checked,
    sentinel: selectors.sentinel.checked,
  };
  return inp
}