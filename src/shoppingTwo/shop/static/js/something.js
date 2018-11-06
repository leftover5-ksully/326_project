let login = document.querySelector('.login');
//login.addEventListener("click", popUp);
let mapIsShown = false;

function popUp(){
		
		let f = document.createElement('form');
		let divOne = document.createElement('div');
		divOne.className = 'form-group';
		let labelOne = document.createElement('label');
		labelOne.innerHTML = 'Email'
		let username = document.createElement('input');
		username.type = 'email'; username.className = 'form-control form-control-sm'; username.placeholder = 'Enter email';
		username.id = 'user';
		divOne.appendChild(labelOne);
		divOne.appendChild(username);
		let divTwo = document.createElement('div');
		let labelTwo = document.createElement('label');
		labelTwo.innerHTML = 'Password'
		let pass = document.createElement('input');
		pass.type = 'password'; pass.className = 'form-control form-control-sm'; pass.placeholder = 'Password'
		pass.id = 'pass';
		divTwo.appendChild(labelTwo);
		divTwo.appendChild(pass);
		let b = document.createElement('button'); b.type = 'submit'; b.className = 'btn btn-primary'; b.innerHTML = 'Submit';
		divTwo.appendChild(b);
		f.appendChild(divOne); f.appendChild(divTwo);
		document.body.appendChild(f);
		
}

function checkInput(){
	let u = document.getElementById('user');
	let p = document.getElementById('pass');
	let uInput = u.value; let pInput = p.value;
	if(uInput !== '' && pInput !== '') alert('Please enter a value!');
}

function doesNotWork(){
	alert("This functionality is disabled!");
}

function addToCart(tar){
	//name
	/*let itemName;
	let cart = document.getElementById('shoppingCart');
	*/
	let listItem = document.createElement('li'); 
	let a = document.createElement('a');
	a.innerHTML = tar.innerHTML; a.href='#';
	listItem.className = 'list-group-item';	
	listItem.onclick = function() {
		this.parentNode.removeChild(this);
	}
	listItem.appendChild(a);
	document.getElementById('shoppingCart').appendChild(listItem);
}

function removeItem(tar){
	tar.parentNode.removeChild(tar);
}

function showMap(){
	if(!mapIsShown){
		let img = document.createElement('img');
		img.className = 'img-fluid';
		img.id = 'shopMap';
		img.src = 'https://fabricasocial.files.wordpress.com/2010/12/craftacular-map-201011.jpg';
		document.body.appendChild(img);
	}
	else{
		let img = document.getElementById('shopMap');
		img.parentNode.removeChild(img);
	}
	
	mapIsShown = !mapIsShown;
}

/*
<form>
	  <div class="form-group">
		<label for="exampleInputEmail1">Email address</label>
		<input type="email" class="form-control form-control-sm" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
	  </div>
	  <div class="form-group">
		<label for="exampleInputPassword1">Password</label>
		<input type="password" class="form-control form-control-sm" id="exampleInputPassword1" placeholder="Password">
	  </div>
	  <button type="submit" class="btn btn-primary">Submit</button>
</form>
*/