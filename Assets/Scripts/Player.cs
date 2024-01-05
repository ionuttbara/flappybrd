using UnityEngine;
using UnityEngine.Events;

[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(Animator))]
public class Player : MonoBehaviour
{
    private Rigidbody rigidbody;
    private Animator animator;

    [SerializeField]
    private float jumpForce;
    [SerializeField]
    private AudioSource getPointSound, dieSound, jumpSound;

    public bool die = false;
    public UnityEvent StartEvent, DieEvent;
    public UnityEvent<int> GetCoinEvent;

    private void Awake()
    {
        rigidbody = GetComponent<Rigidbody>();
        animator = GetComponent<Animator>();
    }

    public void Jump()
    {
        if (!die)
        {
            rigidbody.AddForce(Vector3.up * jumpForce);
            jumpSound.Play();
        }
    }
    public void StartGame()
    {
        rigidbody.isKinematic = false;
        StartEvent.Invoke();
        jumpSound.Play();
    }

    private void Die()
    {
        die = true;
        DieEvent.Invoke();
        dieSound.Play();
        animator.SetBool("Die", true);
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Barrier") && !die)
        {
            Die();
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (!die)
        {
            if (other.gameObject.CompareTag("Coin"))
            {
                GetCoinEvent.Invoke(1);
                getPointSound.Play();
            }
            else if (other.gameObject.CompareTag("Barrier"))
            {
                Die();
            }
        }
    }
}
