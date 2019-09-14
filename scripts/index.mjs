// import { DeviceOrientationControls } from './game/entities/DeviceOrientationControls.mjs';
var scene, camera, renderer, mesh, meshBalloon;
var meshFloor;
var xscale = 0.1, yscale = 0.1, zscale = 0.1;
var radius  = 0.75;

//Camera controls
var controls;

//balloon stuffv
var keyboard = {};
var player = { height:1.8, speed:0.2, turnSpeed:Math.PI*0.02 };
var USE_WIREFRAME = true;

function init(){
	scene = new THREE.Scene();
	camera = new THREE.PerspectiveCamera(90, 1280/720, 0.1, 1000);
	// var controls = new DeviceOrientationControls( camera );
	mesh = new THREE.Mesh(
		new THREE.BoxGeometry(1,1,1),
		new THREE.MeshBasicMaterial({color:0xff4444})
	);
	mesh.position.y += 1; // Move the mesh up 1 meter
	//ascene.add(mesh);
	
  meshBalloon = new THREE.Mesh(
    new THREE.SphereGeometry(radius, 32, 32),
    new THREE.MeshBasicMaterial( { color:0x3b5998 } )
	);
  meshBalloon.position.set(0, 2, 0);
  meshBalloon.scale.set(xscale,yscale,zscale);
 // scene.add (meshBalloon);

	meshFloor = new THREE.Mesh(
		new THREE.PlaneGeometry(40,40, 40,40),
		new THREE.MeshBasicMaterial({color:0xffffff, wireframe:USE_WIREFRAME})
  );
	meshFloor.rotation.x -= Math.PI / 2; // Rotate the floor 90 degrees
	scene.add(meshFloor);


	camera.position.set(0, player.height, -5);
	camera.lookAt(new THREE.Vector3(0,player.height,0));
	
	renderer = new THREE.WebGLRenderer();
	renderer.setSize(1280, 720);
	document.body.appendChild(renderer.domElement);
  
  spawnBalloons();
	animate();
}

function animate(){
	requestAnimationFrame(animate);
	
	mesh.rotation.x += 0.01;
	mesh.rotation.y += 0.02;

	meshBalloon.radius += 1;
	
	// Keyboard movement inputs
	if(keyboard[87]){ // W key
		camera.position.x -= Math.sin(camera.rotation.y) * player.speed;
		camera.position.z -= -Math.cos(camera.rotation.y) * player.speed;
	}
	if(keyboard[83]){ // S key
		camera.position.x += Math.sin(camera.rotation.y) * player.speed;
		camera.position.z += -Math.cos(camera.rotation.y) * player.speed;
	}
	if(keyboard[65]){ // A key
		// Redirect motion by 90 degrees
		camera.position.x += Math.sin(camera.rotation.y + Math.PI/2) * player.speed;
		camera.position.z += -Math.cos(camera.rotation.y + Math.PI/2) * player.speed;
	}
	if(keyboard[68]){ // D key
		camera.position.x += Math.sin(camera.rotation.y - Math.PI/2) * player.speed;
		camera.position.z += -Math.cos(camera.rotation.y - Math.PI/2) * player.speed;
	}
	
	// Keyboard turn inputs
	if(keyboard[37]){ // left arrow key
		camera.rotation.y -= player.turnSpeed;
	}
	if(keyboard[39]){ // right arrow key
		camera.rotation.y += player.turnSpeed;
  }
  if(keyboard[38]){ // up key
    camera.position.y += 0.1;
  }
  if(keyboard[40]){ // down key
    camera.position.y -= 0.1;
  }

  // controls.update();

	renderer.render(scene, camera);
}

function keyDown(event){
	keyboard[event.keyCode] = true;
}

function keyUp(event){
	keyboard[event.keyCode] = false;
}

function spawnBalloons(){
	scene.add (meshBalloon);
	
	xscale += 200000;
	renderer.render(scene, camera);
}

window.addEventListener('keydown', keyDown);
window.addEventListener('keyup', keyUp);

window.onload = init;