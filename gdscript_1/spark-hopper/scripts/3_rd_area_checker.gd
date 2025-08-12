extends Area2D


func _on_body_entered(body: Node2D) -> void:
	if body.name == "player":
		$AnimationPlayer3.play("spark_costs")
		$CollisionShape2D.disabled
