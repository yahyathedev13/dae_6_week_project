extends CharacterBody2D

# variable that show in inspecter

@export var movement_speed : float = 200.0
@export var jump_force : float = -250.0
@export var max_spark : int = 100
@export var max_health : int = 3

# variables that show only on the scripting thing

var spark : int = max_spark
var health : int = max_health
var is_frozen : bool = false
var has_key : bool = false

var facing_direction := 1

# gravity constant

const GRAVITY : float = 800.0

func _physics_process(delta: float) -> void:
	
	# controls the Gravity
	
	if not is_on_floor():
		velocity.y += GRAVITY * delta
		if velocity.y < 0:
			$AnimatedSprite2D.play("jump")
		else:
			$AnimatedSprite2D.play("fall")
		
	else:
		velocity.y = 0
	
	# Movement L/R
	
	if Input.is_action_pressed("run_right"):
		facing_direction = 1
		velocity.x = movement_speed
		$AnimatedSprite2D.flip_h = false
		if is_on_floor():
			$AnimatedSprite2D.play("running")
	
	elif Input.is_action_pressed("run_left"):
		facing_direction = -1
		velocity.x = -movement_speed
		$AnimatedSprite2D.flip_h = true
		if is_on_floor():
			$AnimatedSprite2D.play("running")
	
	else:
		velocity.x = 0
		if is_on_floor():
			$AnimatedSprite2D.play("idle")
	
	# movement pt2 jumpinng
	
	if Input.is_action_just_pressed("jump") and is_on_floor() and max_spark >= 20:
		velocity.y = jump_force
		spark -= 20
	
	move_and_slide()
	
	
	
