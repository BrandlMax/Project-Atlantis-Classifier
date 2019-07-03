using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Magic : MonoBehaviour
{

    public string State = "20";

    public GameObject jump;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(State == "0")
        {
            this.transform.position = Vector3.Lerp(this.transform.position, jump.transform.position, 1);
        }
        if(State == "1")
        {
            this.transform.position = new Vector3(this.transform.position.x, this.transform.position.y - 10, this.transform.position.z);
            State = "20";
        }
    }
}
