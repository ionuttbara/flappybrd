using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Spawner : MonoBehaviour
{
    [SerializeField]
    private List<GameObject> variants;
    [SerializeField]
    private float offsetSpawn;
    [SerializeField]
    private Transform pointSpawn;

    private int numberLastVariant = 0;
    private bool spawn = true;

    private int RandomVariant()
    {
        int n = Random.Range(0, variants.Count);

        if (numberLastVariant == n)
            n = RandomVariant();

        numberLastVariant = n;

        return n;
    }

    public void EndSpawn() 
    {
        spawn = false;
    }
    public void StartSpawn()
    {
        StartCoroutine(Spawn());
    }

    private IEnumerator Spawn()
    {
        while (spawn)
        {
            int numberVariant = RandomVariant();
            Instantiate(variants[numberVariant], pointSpawn.position, pointSpawn.rotation);
            yield return new WaitForSeconds(offsetSpawn);
        }
    }
}
