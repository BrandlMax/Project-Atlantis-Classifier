using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Magic : MonoBehaviour
{

    public string State = "20";
    public string TState = "0";
    public string OldState = "";

    public Animator anim;

    // Start is called before the first frame update
    void Start()
    {
        anim = GetComponent<Animator>();
        anim.Play("DolphinNormal");
    }

    // Update is called once per frame
    void Update()
    {
        Debug.Log(State);
        switch (State)
        {
            case "noFinger":
                TState = "0";
                break;
            case "OneFinger":
                TState = "1";
                break;
            case "HandDown":
                TState = "2";
                break;
        }


        // NO FINGER
        if (TState == "0")
        {
            anim.SetBool("isRising", false);
            anim.SetBool("isSinking", false);
        }

        // ONE FINGER
        if (TState == "1")
        {
            anim.SetBool("isSinking", false);
            anim.SetBool("isRising", true);
        }

        // HAND
        if (TState == "2")
        {
            anim.SetBool("isRising", false);
            anim.SetBool("isSinking", true);
        }
    }
}
