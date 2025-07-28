extends CharacterBody2D

@export var movement_speed := 100
@export var jump_force := -250
@export var gravity_force := 600
@export var jump_spark_cost := 1

var spark := 5
var is_frozen := false
var facing_direction := 1

func _physics_process(delta: float) -> void:
	if is_frozen == true:
		velocity = Vector2.ZERO
		$AnimatedSprite2D.play("frozen")
		
