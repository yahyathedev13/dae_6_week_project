extends Area2D


var player_in_area : bool = false

func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		player_in_area = true
		if body.can_be_hurt:
			body.hurt()

func _process(delta: float) -> void:
	if player_in_area:
		for body in get_overlapping_bodies():
			if body.is_in_group("player") and body.can_be_hurt:
				body.hurt() 
