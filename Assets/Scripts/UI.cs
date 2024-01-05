using System;
using UnityEngine;
using UnityEngine.UI;

public class UI : MonoBehaviour
{
    [SerializeField]
    private Text coinText;
    [SerializeField]
    private Text recordText;

    [SerializeField]
    private GameObject endPanel;
    [SerializeField]
    private GameObject startText;

    public void ChangeCoinText(int value)
    {
        coinText.text = value.ToString();
    }

    public void SetRecordText(int value)
    {
        recordText.text = String.Format("High Score: {0}", value);
    }

    public void EnableEndPanel()
    {
        endPanel.SetActive(true);
    }

    public void DisableStartPanel()
    {
        startText.SetActive(false);
    }
}
