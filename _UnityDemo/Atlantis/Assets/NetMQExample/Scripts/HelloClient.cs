using UnityEngine;

public class HelloClient : MonoBehaviour
{
    private HelloRequester _helloRequester;

    public GameObject box;
    public bool run;

    private void Start()
    {
        _helloRequester = new HelloRequester();
        _helloRequester.Start();

        _helloRequester.box = box.GetComponent<Magic>();
        _helloRequester.run = run;
    }

    private void OnDestroy()
    {
        _helloRequester.Stop();
    }
}