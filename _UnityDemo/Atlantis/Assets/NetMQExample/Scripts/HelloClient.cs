using UnityEngine;

public class HelloClient : MonoBehaviour
{
    private HelloRequester _helloRequester;

    public GameObject box;

    private void Start()
    {
        _helloRequester = new HelloRequester();
        _helloRequester.Start();

        _helloRequester.box = box.GetComponent<Magic>();
    }

    private void OnDestroy()
    {
        _helloRequester.Stop();
    }
}