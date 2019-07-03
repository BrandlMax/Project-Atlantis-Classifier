using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Magic : MonoBehaviour
{

    public string State = "20";
    public string TState = "20";

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(TState == "0")
        {
            Debug.Log("0");
        }
        if(TState == "1")
        {
            // this.transform.position = new Vector3(this.transform.position.x, this.transform.position.y - 10, this.transform.position.z);
            Debug.Log("1");
        }
        if (TState == "2")
        {
            // this.transform.position = new Vector3(this.transform.position.x, this.transform.position.y - 10, this.transform.position.z);
            Debug.Log("2");
        }
    }
}
