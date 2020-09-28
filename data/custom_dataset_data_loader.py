import torch.utils.data
from data.dataset import DatasetFactory


class CustomDatasetDataLoader:
    def __init__(self, opt, is_for_train=True):
        self._opt = opt
        self._is_for_train = is_for_train
        self._num_threds = opt.n_threads_train if is_for_train else opt.n_threads_test
        self._create_dataset()

    def _create_dataset(self):
        self._dataset = DatasetFactory.get_by_name(self._opt.dataset_mode, self._opt, self._is_for_train)
        # print('self._dataset',self._dataset,self._opt.dataset_mode,self._opt)
        self._dataloader = torch.utils.data.DataLoader(
            self._dataset,
            batch_size=self._opt.batch_size,
            shuffle=True,
            num_workers=int(self._num_threds),
            num_workers = 4,
            drop_last=True)

    def load_data(self):
        return self._dataloader

    def __len__(self):
        return len(self._dataset)
