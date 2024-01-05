using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class Move : MonoBehaviour
{
    [SerializeField]
    private float speed;
    [SerializeField]
    private float timeLive;

    private bool move = true;
    private Player player;

    private void Awake()
    {
        player = GameObject.FindObjectOfType<Player>();
        player.DieEvent.AddListener(() =>
        {
            move = false;
        });
    }

    private void Start()
    {
        StartCoroutine(TimeToDie());
    }

    private void Update()
    {
        if (move)
            transform.Translate(Vector3.left * speed * Time.deltaTime);
    }

    private IEnumerator TimeToDie()
    {
        yield return new WaitForSeconds(timeLive);
        if (move)
        {
            Destroy(gameObject);
        }
    }
}