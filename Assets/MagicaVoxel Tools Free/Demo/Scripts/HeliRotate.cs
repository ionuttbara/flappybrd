using UnityEngine;

public class HeliRotate : MonoBehaviour
{
    public Vector3 axis;
    public float speed = 1;

    private void Update()
    {
        this.transform.Rotate(axis, speed * Time.deltaTime);
    }
}