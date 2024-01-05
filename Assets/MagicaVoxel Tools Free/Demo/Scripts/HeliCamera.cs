using UnityEngine;

public class HeliCamera : MonoBehaviour
{
    public GameObject target;
    public Vector3 offset;

    // Use this for initialization
    private void Start()
    {
    }

    // Update is called once per frame
    private void Update()
    {
        this.transform.position = target.transform.position + offset;
        this.transform.LookAt(target.transform);
    }
}