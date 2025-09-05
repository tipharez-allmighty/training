def retry(times: int = 3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise Exception(f"Failed after {times} attempts.") 
        return wrapper
    
    return decorator


@retry()
def main():
    raise

if __name__ == "__main__":
    main()
