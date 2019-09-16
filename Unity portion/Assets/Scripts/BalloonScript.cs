using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class BalloonScript : MonoBehaviour
{
    public Text countText;

    private int score = 0;
    private Rigidbody balloonInstance;
    private bool balloonSpawned;
    private float ballonTime;
    private Vector3 temp;

    // Start is called before the first frame update
    void Start()
    {
        balloonInstance = GetComponent<Rigidbody>();
        balloonInstance.isKinematic = true;
        ballonTime = Time.time;
        balloonSpawned = true;
      
        setCountText();
        Instantiate(countText, this.transform, false);
    }

    // Update is called once per frame
    void Update()
    {
        if (balloonSpawned == true)
        {
            temp = balloonInstance.transform.localScale;
            temp += new Vector3(Time.deltaTime, Time.deltaTime, Time.deltaTime);
            balloonInstance.transform.localScale = temp;
            balloonInstance.position = transform.position;
            balloonInstance.rotation = transform.rotation;
            if ((Time.time - ballonTime) >= 0.7)
            {
                balloonInstance.isKinematic = false;
                balloonSpawned = false;
                this.transform.position = new Vector3(this.transform.position.x, this.transform.position.y + Time.deltaTime, this.transform.position.z);
                print("here");
            }
        }
    }

    public void destroyBalloon()
    {
        Destroy(this.gameObject);
    }

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "ceiling")
        {
            score += 1;
            Destroy(gameObject);
            print("WOOO");
            setCountText();
        }

    }

    void setCountText()
    {
        countText.text = "Score: " + score.ToString();
    }
}
