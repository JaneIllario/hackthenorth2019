using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameScript : MonoBehaviour
{
    public GameObject BalloonPrefab;
    private float nextActionTime = 5.0f;
    // Start is called before the first frame update
    void Start()
    {
       // Instantiate(BalloonPrefab, new Vector3(0, 2, 0), Quaternion.identity);
       // Instantiate(BalloonPrefab, new Vector3(1, 2, 0), Quaternion.identity);
    }

    // Update is called once per frame
    void Update()
    {
        if (Time.time > nextActionTime)
        {
            print("ye");

            nextActionTime += 5.0f;
            int res = Random.Range(0, 4);
            spawnBalloon(res);
        }
    }

    void spawnBalloon(int res)
    {
        if(res == 0)
        {
            Instantiate(BalloonPrefab, new Vector3(-2.0f, 2.0f, -2.5f), Quaternion.identity);
            print("a");
        }
        if (res == 1)
        {
            Instantiate(BalloonPrefab, new Vector3(2.0f, 2.0f, 2.5f), Quaternion.identity);
            print("b");
        }
        if (res == 2)
        {
            Instantiate(BalloonPrefab, new Vector3(0.0f, 2.0f, 2.5f), Quaternion.identity);
            print("c");
        }
        if (res == 3)
        {
            Instantiate(BalloonPrefab, new Vector3(2.5f, 2.0f, 0.0f), Quaternion.identity);
            print("d");
        }
        if (res == 4)
        {
            Instantiate(BalloonPrefab, new Vector3(3.0f, 2, -1.0f), Quaternion.identity);
            print("e");
        }
    }
}
