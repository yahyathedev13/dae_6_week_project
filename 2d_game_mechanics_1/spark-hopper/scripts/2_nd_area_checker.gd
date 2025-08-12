extends Area2D


func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		$AnimationPlayer2.play("mission_label")
		$CollisionShape2D.disabled
