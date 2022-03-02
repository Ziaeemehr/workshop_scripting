import argparse


def Main():

    parser = argparse.ArgumentParser()


    parser.add_argument('-n',
                        "--nohup",
                        help="(default: False) submit jobs with nohup to store jobIds.",
                        action="store_true")
    

    parser.add_argument("-cl", "--clean",
                        help="(default: True) clean output directory.",
                        action="store_false")

    # parser.add_argument("-c", "--continueJobs",
    #                     help="(default: False) continue the the jobs from where it lefted, without clearing the output directory.",
    #                     action="store_true")

    args = parser.parse_args()
    print(f"clean:        {args.clean}")
    print(f"nohup:        {args.nohup}")
    # print(f"continueJobs: {args.continueJobs}")


if __name__ == "__main__":

    Main()
