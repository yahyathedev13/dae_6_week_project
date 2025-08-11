extends CharacterBody2D

# variable that show in inspecter

@export var movement_speed : float = 200.0
@export var jump_force : float = -375.0
@export var max_spark : int = 20
@export var max_health : int = 3

# onready variables

@onready var main_camera = $main_player_camera
@onready var camera_anim = main_camera.get_node("AnimationPlayer")

# Not yet defined

var spark_bar
var spark_label
var health_bar
var health_label
var Jump_label_indicater
var dash_label_indicater
var jumps_remaining 
var UI_anim

# variables that show only on the scripting thing

var facing_direction := 1
var spark : int = max_spark
var health : int = max_health
var is_frozen : bool = false
var has_key : bool = false
var can_be_hurt : bool = true
var is_dead : bool = false
var invinsible : bool = false
var regen : bool = false
var can_jump  : bool = true

# gravity constant

const GRAVITY : float = 1500.0

# READY FUNCTION

func _ready() -> void:
	
	print("jump_force:", jump_force)
	
	spark_bar = get_node("/root/main_game_UI/spark_bar")
	spark_label = get_node("/root/main_game_UI/spark_label")
	
	health_bar = get_node("/root/main_game_UI/health_bar")
	health_label = get_node("/root/main_game_UI/health_label")
	
	Jump_label_indicater = get_node("/root/main_game_UI/label/Jump_label_indicater")
	
	UI_anim = get_node("/root/main_game_UI/UI_anim")
	


# MAINGAME LOOP 

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
	
	if Input.is_action_pressed("run_right") :
		facing_direction = 1
		velocity.x = movement_speed
		$AnimatedSprite2D.flip_h = false
		if is_on_floor():
			$AnimatedSprite2D.play("running")
	
	elif Input.is_action_pressed("run_left") :
		facing_direction = -1
		velocity.x = -movement_speed
		$AnimatedSprite2D.flip_h = true
		if is_on_floor():
			$AnimatedSprite2D.play("running")
			
	
	else:
		velocity.x = 0
		if is_on_floor() :
			$AnimatedSprite2D.play("idle")
	
	# movement pt2 jumpinng
	
	if Input.is_action_just_pressed("jump") and is_on_floor() and spark >= 3 and can_jump:
		velocity.y = jump_force
		spark -= 3
	 
	elif jumps_remaining == 0 and can_jump == false and Input.is_action_just_pressed("jump") and is_on_floor():
		UI_anim.play("spark_too_low")

	
	move_and_slide()

func _process(float) -> void:
	
	jumps_remaining = spark / 3
	
	if spark < 3:
		can_jump = false
	else:
		can_jump = true
	
	
	
	# Bars
	
	spark_bar.value = spark
	spark_label.text = "            %d " % [spark]
	
	health_bar.value = health
	health_label.text = "                %d " % [health ]
	
	Jump_label_indicater.text = "JUMP    %d" % [jumps_remaining]
	
	# handling spark re-gen
	
	if spark < max_spark and regen == false:
		regen = true
		$spark_timer.start()

# hurt function

func hurt():
	
	if can_be_hurt == true and is_dead == false:
		camera_anim.play("rattle")
		$player_anim2.play("hurt")
		health -= 1
		can_be_hurt = false
		
		if can_be_hurt == false:
			$Timer.start()
			$player_anim.play("blinking")
		
		
	if health <= 0:
		is_dead = true
	if is_dead == true:
		$player_anim.play("RESET")
		$AnimatedSprite2D.play("death")
		set_physics_process(false)
		$death_timer.start()

# timers

func _on_timer_timeout() -> void:
	can_be_hurt = true
	$player_anim.play("RESET")

func _on_death_timer_timeout() -> void:
	get_tree().reload_current_scene()

func _on_spark_timer_timeout() -> void:
	if spark < 20:
		spark += 1
		$spark_timer.start()
