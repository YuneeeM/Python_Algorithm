//4. 객체 - 값을 받는 그릇이라는 관점

var grades = { 'egoing': 10, 'k8805': 6, 'sorialgi': 80 }; //key-value

var grades1 = {};
grades1['egoing'] = 10;
grades1['k8805'] = 6;
grades1['sorialgi'] = 80;

console.log(grades['egoing']);
console.log(grades['ego' + 'ing']);
//하지만 grades.'ego'+'ing'; 는 안된다!
console.log(grades.egoing); //더 간결함

//----------------------------------------------

for (key in grades) {
  console.log("key : " + key + " value : " + grades[key]);
}

//-------------------------------------------------

var gradess = {
  'list': { 'egoing': 10, 'k8805': 8, 'sorialgi': 80 },
  'show': function () {
    console.log('Hello World!');
    console.log(this.list);
    for (var name in this.list) {
      console.log(name, this.list[name])
    }
  }
}

console.log(gradess['list']['egoing']);
gradess['show']();
gradess.show();