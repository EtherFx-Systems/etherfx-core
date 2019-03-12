import redis
import dill

redis_client = redis.Redis(
    host="35.193.40.68", port=6379, db=0
)  # Make connection to Redis instance running locally


class GDSClient:
    def test_import(self):
        print("Import Successful")

    def add_args_to_gds(self, task_id, list_of_args):
        """Check if this key already exists"""
        if self.check_key_exists_in_gds(
            task_id
        ):  # Returns number of keys found - should be 0
            raise Exception(
                "Task ID already has arguments/results stored in the GDS"
            )  # Temporary - Replace by EtherFx error

        return self.insert_in_key_list_redis(task_id, list_of_args)

    def get_args_from_gds(self, task_id):
        if not self.check_key_exists_in_gds(task_id):
            raise Exception(
                "Task ID not found on GDS"
            )  # Temporary - Replace by EtherFx error
        return retrieve_value_list_for_key_gds(task_id)

    def retrieve_value_list_for_key_gds(self, redis_key):
        number_of_vals = redis_client.llen(redis_key)
        vals_retrieved = redis_client.lrange(redis_key, 0, number_of_vals - 1)

        return vals_retrieved if vals_retrieved else None

    def check_key_exists_in_gds(self, task_id):
        if redis_client.exists(task_id) > 0:
            return True
        else:
            return False

    def insert_in_key_list_redis(self, task_id, values_to_be_added):
        try:
            for x in values_to_be_added:
                # print type(x)
                redis_client.rpush(task_id, x)
        except Exception as e:
            print(e)
        return True

    def get_result_from_gds(self, task_id):
        if not self.check_key_exists_in_gds(task_id):
            raise Exception("Task ID does not exist on the GDS.")
        else:
            return self.retrieve_value_list_for_key_gds(task_id)

    def get_result_from_gds_noexcept(self, task_id):
        if self.check_key_exists_in_gds(task_id):
            return self.retrieve_value_list_for_key_gds(task_id+"_result")
        else:
            return None

    def set_result_in_gds(self, task_id, execution_result):
        """
            TODO: Figure out if errors need to be stored as elements as opposed to the first (and only) element of the list
        """
        if not task_id: return
        return self.insert_in_key_list_redis(task_id+"_result", execution_result)

    def clear_gds_for_task_id(self, task_id):
        if redis_client.exists(task_id) > 0:
            redis_client.delete(task_id)
            return True
        else:
            return False


def main():
    # test_obj = sample_class()
    args = ["abc", "def", "ghi"]
    # clear_gds_for_task_id("fooda")
    # print add_args_to_gds("fooda", args)
    cl = GDSClient()
    print(cl.retrieve_value_list_for_key_gds("3ece0261-b0e1-481f-b460-e9c3594761b9"))
    # print get_args_from_gds("fooda")


if __name__ == "__main__":
    main()
