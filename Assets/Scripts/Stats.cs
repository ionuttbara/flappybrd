using UnityEngine;
using UnityEngine.Events;

public class Stats : MonoBehaviour
{
    public UnityEvent<int> ChangeCoinsEvent, SetRecordEvent;

    [SerializeField]
    private int coin;

    private int record;

    private void Awake()
    {
        record = PlayerPrefs.GetInt("Record");
        SetRecordEvent.Invoke(record);
        ChangeCoins(0);
    }

    public void ChangeCoins(int value)
    {
        coin += value;
        ChangeCoinsEvent.Invoke(coin);
    }

    public void CheckRecord()
    {
        if (coin > record)
        {
            PlayerPrefs.SetInt("Record", coin);
            SetRecordEvent.Invoke(coin);
        }
    }
}
